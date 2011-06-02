/*
 * main.cpp
 *
 *  Created on: May 31, 2011
 *      Author: sbobovyc
 */

#include <iostream>
#include <vector>
#include "Blob.hpp"
#include "Utils.hpp"

using namespace std;
using namespace Magick;

int main(int argc, char ** argv)
{
	vector<int> color; // (0,0,0);
	int height = 10;
	int width = 10;
	int canvas_height = 800;
	int canvas_width = 800;
	int max_level = 4;
	pair<int,int> seed_coords (400,400);
	int distribution[8] = {90,90,90,90,90,90,90,90};

	map<Color, unsigned long> image_histogram = DCS::create_histogram("image.jpeg");
	vector<Color> color_list = DCS::calculate_colors(image_histogram, 3);

//	for(int i = 0; i < int(color_list.size()); i++)
//		cout << color_list[i].redQuantum() << " " << color_list[i].greenQuantum() << " " << color_list[i].blueQuantum() << endl;
	Color base_color = DCS::calculate_base_color(color_list);
//	cout << base_color.redQuantum() << " " << base_color.greenQuantum() << " " << base_color.blueQuantum() << endl;

	vector<int> color1;
	color1.push_back(color_list[0].redQuantum());
	color1.push_back(color_list[0].greenQuantum());
	color1.push_back(color_list[0].blueQuantum());
	Image image = Image(Geometry(canvas_width, canvas_height), base_color);

	DCS::draw_blobs(1, color1, width, height, canvas_width, canvas_height, max_level, distribution, &image);
	image.write("out.png");
	return 0;
}
