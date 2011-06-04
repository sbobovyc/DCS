/*
 * Utils.cpp
 *
 *  Created on: May 31, 2011
 *      Author: sbobovyc
 */

#include <time.h>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>
#include <map>
#include <iostream>
#include <iomanip>

#include <Magick++.h>
#include <libnoise/noise.h>

#include "DCS.hpp"

using namespace std;
using namespace Magick;
using namespace noise;

namespace DCS {
DCS_histogram create_histogram(const string &image_path)
{
	cout << image_path << endl;
	Image image(image_path);
	DCS_histogram histogram;
	colorHistogram(&histogram, image);

	return histogram;
}

void print_histogram(const DCS_histogram &histogram)
{
	std::map<Color,unsigned long>::const_iterator p=histogram.begin();
	  while (p != histogram.end())
	    {
	      cout << setw(10) << (int)p->second << ": ("
	           << setw(10) << ((int)p->first.redQuantum() / 65536.0) * 255.0 << ","
	           << setw(10) << ((int)p->first.greenQuantum() / 65536.0) * 255.0 << ","
	           << setw(10) << ((int)p->first.blueQuantum() / 65536.0) * 255.0 << ")"
	           << endl;
	       p++;
	    }
}

void partition_histogram()
{

}

DCS_color_list calculate_colors(DCS_histogram color_histogram, int number_of_colors)
{
	DCS_color_list color_list;

	// convert map to vector
	std::vector<std::pair<Color, unsigned long> > color_vector(color_histogram.begin(), color_histogram.end());

	//for(int i = 0; i < color_vector.size(); i++)
		//cout << color_vector[i].first.redQuantum() << " " << color_vector[i].first.greenQuantum() << " " << color_vector[i].first.blueQuantum() << endl;

	// 1. Figure out bin sizes
	// 2. Partition histogram according to those bin sizes
	// 3. Do a weighted average on each bin

	// Start 1
	int bin_size = color_histogram.size() / number_of_colors;
	// End 1

	// Start 2
	// if the number of colors int the histogram is not even, the first bin is the largest bin
	vector< pair<int,int> > bin_list;
	if(color_histogram.size() % number_of_colors == 0)
	{
		for(int i = 0; i < number_of_colors; i++)
		{
			bin_list.push_back( pair<int,int> ((i*bin_size),i*bin_size+bin_size-1) );
		}
	} else {
		bin_list.push_back( pair<int,int> (0,bin_size) );
		for(int i = 1; i < number_of_colors; i++)
		{
			bin_list.push_back( pair<int,int> ((i*bin_size+1),(i*bin_size)+bin_size) );
		}
	}
	// End 2

	for(int i = 0; i < bin_list.size(); i++)
		cout << bin_list[i].first << " " << bin_list[i].second << endl;

	// Start 3
	unsigned long tmp_red = 0;
	unsigned long tmp_green = 0;
	unsigned long tmp_blue = 0;
	unsigned long weight = 0;

	for(int i = 0; i < int(bin_list.size()); i++)
	{
		weight = 0;
		for(int j = bin_list[i].first; j <= bin_list[i].second; j++)
		{
			//cout << color_vector[j].first.redQuantum() << " " << color_vector[j].first.greenQuantum() << " " << color_vector[j].first.blueQuantum() << endl;
			tmp_red += color_vector[j].first.redQuantum() * color_vector[j].second;
			tmp_green += color_vector[j].first.greenQuantum() *  color_vector[j].second;
			tmp_blue += color_vector[j].first.blueQuantum() * color_vector[j].second;
			weight += color_vector[j].second;
		}
		unsigned long num_elements = weight;
//		int num_elements = (bin_list[i].second - bin_list[i].first);
		color_list.push_back(pair<Magick::Color, unsigned long> (Color(tmp_red / num_elements, tmp_green / num_elements, tmp_blue / num_elements), num_elements) );
		tmp_red = 0;
		tmp_green = 0;
		tmp_blue = 0;
	}

	return color_list;
}

//TODO add weighted average to base color calculation
Color calculate_base_color(DCS_color_list colors)
{
	unsigned long red = 0;
	unsigned long blue = 0;
	unsigned long green = 0;
	unsigned long weight = 0;

	for(int i = 0; i < int(colors.size()); i++)
	{
		red += colors[i].first.redQuantum() * colors[i].second;
		green += colors[i].first.greenQuantum() * colors[i].second;
		blue += colors[i].first.blueQuantum() * colors[i].second;
		weight += colors[i].second;
	}
	red /= weight;
	green /= weight;
	blue /= weight;

	return Color(red, green, blue);
}

void draw_blobs(DCS_color color, int canvas_width, int canvas_height, const int octave_count, const double frequency, const double persistence, const int seed, const double threshold, const double z, Image * image)
{
	Magick::Color current_color = Magick::Color(color.red, color.green, color.blue);
	module::Perlin module;
	module.SetOctaveCount(octave_count);
	module.SetFrequency(frequency);
	module.SetPersistence(persistence);
	module.SetSeed(seed);

	for(int i = 0; i < canvas_width; i++)
	{
		for(int j = 0; j < canvas_height; j++)
		{
			double value = module.GetValue(i, j, z);
			//cout << i << " " << j << " " << value << endl;
			if(value > threshold)
				(*image).pixelColor(i, j, current_color);
		}
	}
}

void draw_blobs(int count, vector<int> color, int width, int height, int canvas_width, int canvas_height, int max_level, int distribution[8], Image * image)
{
	(*image).strokeColor("red"); // Outline color
	(*image).strokeWidth(2);
	srand(time(NULL));
	pair<int,int> seed_coords (rand() % canvas_height + 2, rand() % canvas_width + 2);

	for(int i = 0; i < count; i++)
	{
		DCS_Blob blob = DCS_Blob(color, height, width, canvas_width, canvas_height, max_level, seed_coords, distribution);
		cout << blob << endl;
		std::vector< std::pair< std::pair<int,int>, std::pair<int,int> > > rectangle_list = blob.get_rectangle_list();
		for(int j = 0; j < int(rectangle_list.size()); j++)
		{
			(*image).draw(DrawableRectangle(rectangle_list[j].first.first, rectangle_list[j].first.second, rectangle_list[j].second.first, rectangle_list[j].second.second));
		}
	}

}

}
