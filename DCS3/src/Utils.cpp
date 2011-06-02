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
#include <Magick++.h>
#include <iostream>
#include <iomanip>

#include "Blob.hpp"

using namespace std;
using namespace Magick;

namespace DCS {
map<Color, unsigned long> create_histogram(string image_path)
{
	Image image(image_path);
	map<Color, unsigned long> histogram;
	colorHistogram(&histogram, image);
	/*
	std::map<Color,unsigned long>::const_iterator p=histogram.begin();
	  while (p != histogram.end())
	    {
	      cout << setw(10) << (int)p->second << ": ("
	           << setw(10) << (int)p->first.redQuantum() << ","
	           << setw(10) << (int)p->first.greenQuantum() << ","
	           << setw(10) << (int)p->first.blueQuantum() << ")"
	           << endl;
	       p++;
	    }
	*/

	return histogram;
}

void partition_histogram()
{

}

vector<Color> calculate_colors(map<Color, unsigned long> color_histogram, int number_of_colors)
{
	vector<Color> color_list;
	vector<unsigned long> tmp_color_list(3);
	int bin_size = color_histogram.size() / number_of_colors;
	std::vector<std::pair<Color, unsigned long> > color_vector(color_histogram.begin(), color_histogram.end());

	// 1. Figure out bin sizes
	// 2. Partition histogram according to those bin sizes
	// 3. Do a weighted average on each bin

	// divide the histogram into almost equal bins
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

	// start weighted average
	for(int i = 0; i < int(bin_list.size()); i++)
	{
		unsigned long weight = 0;
		for(int j = bin_list[i].first; j <= bin_list[i].second; j++)
		{
//			tmp_color_list[0] += color_vector[j].first.redQuantum();
//			tmp_color_list[1] += color_vector[j].first.greenQuantum();
//			tmp_color_list[2] += color_vector[j].first.blueQuantum();

			tmp_color_list[0] += color_vector[j].first.redQuantum() * color_vector[j].second;
			tmp_color_list[1] += color_vector[j].first.greenQuantum() * color_vector[j].second;
			tmp_color_list[2] += color_vector[j].first.blueQuantum() * color_vector[j].second;
			weight += color_vector[j].second;

//			cout << color_vector[j].first.redQuantum() << endl;
//			cout << color_vector[j].first.greenQuantum() << endl;
//			cout << color_vector[j].first.blueQuantum() << endl;
		}
		unsigned long num_elements = weight;
//		int num_elements = (bin_list[i].second - bin_list[i].first);
		color_list.push_back(Color(tmp_color_list[0] / num_elements, tmp_color_list[1] / num_elements, tmp_color_list[2] / num_elements));
	}

	return color_list;
}

//TODO add weighted average to base color calculation
Color calculate_base_color(vector<Color> colors)
{
	unsigned long red = 0;
	unsigned long blue = 0;
	unsigned long green = 0;

	for(int i = 0; i < int(colors.size()); i++)
	{
		red += colors[i].redQuantum();
		green += colors[i].greenQuantum();
		blue += colors[i].blueQuantum();
	}
	red /= colors.size();
	green /= colors.size();
	blue /= colors.size();

	return Color(red, green, blue);
}

void draw_blobs(int count, vector<int> color, int width, int height, int canvas_width, int canvas_height, int max_level, int distribution[8], Image * image)
{
	srand(time(NULL));
	pair<int,int> seed_coords (rand() % height + 2, rand() % width + 2);

	for(int i = 0; i < count; i++)
	{
		DCS_Blob blob = DCS_Blob(color, height, width, canvas_width, canvas_height, max_level, seed_coords, distribution);
		std::vector< std::pair< std::pair<int,int>, std::pair<int,int> > > rectangle_list = blob.get_rectangle_list();
		for(int j = 0; i < int(rectangle_list.size()); j++)
		{
			(*image).draw(DrawableRectangle(rectangle_list[i].first.first, rectangle_list[i].first.second, rectangle_list[i].second.first, rectangle_list[i].second.second));
		}
	}
}

}
