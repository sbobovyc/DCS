/*
 * Utils.cpp
 *
 *  Created on: May 31, 2011
 *      Author: sbobovyc
 */

//TODO Make a weighted average function

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

namespace DCS {

bool great2small (std::pair<Magick::Color, unsigned long> i, std::pair<Magick::Color, unsigned long> j) { return (i.second>j.second); }

DCS_histogram create_histogram(const string &image_path)
{
	Magick::Image image(image_path);
	DCS_histogram histogram;
	Magick::colorHistogram(&histogram, image);

	return histogram;
}

void sort_color_vector(DCS_color_vector &color_vector)
{
	sort(color_vector.begin(), color_vector.end(), great2small);
}

void print_histogram(const DCS_histogram &histogram)
{
	DCS::DCS_histogram::const_iterator p=histogram.begin();
	  while (p != histogram.end())
	    {
	      cout << setw(10) << (int)p->second << ": ("
	           << setw(10) << (int)p->first.redQuantum() << ","
	           << setw(10) << (int)p->first.greenQuantum() << ","
	           << setw(10) << (int)p->first.blueQuantum() << ")"
	           << endl;
	       p++;
	    }
}

void print_color_vector(const DCS_color_vector &color_vector)
{
	for(unsigned int i = 0; i < color_vector.size(); i++)
		cout << "Color : " << color_vector[i].first.redQuantum() << " "
							<< color_vector[i].first.greenQuantum() << " "
							<< color_vector[i].first.blueQuantum() << " "
							<< "Weight : " << color_vector[i].second << endl;
}

void partition_histogram()
{

}

DCS_color_vector calculate_colors(DCS_histogram color_histogram, int number_of_colors)
{
	DCS_color_vector color_list;

	// convert map to vector
	std::vector<std::pair<Magick::Color, unsigned long> > color_vector(color_histogram.begin(), color_histogram.end());

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

	// Start 3
	unsigned long tmp_red = 0;
	unsigned long tmp_green = 0;
	unsigned long tmp_blue = 0;
	unsigned long weight = 0;

	for(unsigned int i = 0; i < bin_list.size(); i++)
	{
		weight = 0;
		for(int j = bin_list[i].first; j <= bin_list[i].second; j++)
		{
			tmp_red += color_vector[j].first.redQuantum() * color_vector[j].second;
			tmp_green += color_vector[j].first.greenQuantum() *  color_vector[j].second;
			tmp_blue += color_vector[j].first.blueQuantum() * color_vector[j].second;
			weight += color_vector[j].second;
		}
		unsigned long num_elements = weight;
//		int num_elements = (bin_list[i].second - bin_list[i].first);
		color_list.push_back(pair<Magick::Color, unsigned long> (Magick::Color(tmp_red / num_elements, tmp_green / num_elements, tmp_blue / num_elements), num_elements) );
		tmp_red = 0;
		tmp_green = 0;
		tmp_blue = 0;
	}

	return color_list;
}


Magick::Color calculate_base_color(DCS_color_vector colors)
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

	return Magick::Color(red, green, blue);
}

//TODO This function needs to be able to have a Perlin noise as an input
void draw_blobs(Magick::Color color, int canvas_width, int canvas_height, const int octave_count, const double frequency, const double persistence, const int seed, const double threshold, const double z, Magick::Image * image)
{
	noise::module::Perlin module;
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
				(*image).pixelColor(i, j, color);
		}
	}
}

}
