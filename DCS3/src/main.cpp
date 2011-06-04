/*
 * main.cpp
 *
 *  Created on: May 31, 2011
 *      Author: sbobovyc
 */

#include <iostream>
#include <vector>

#include "DCS.hpp"

using namespace std;
using namespace Magick;

int main(int argc, char ** argv)
{
	int num_colors = 2;
	int canvas_height = 800;
	int canvas_width = 800;
	int octave_count = 2;
	double frequency = 0.02;
	double persistence = 0.1;
	double threshold = 0.1;
	double z = 0.3;

	DCS::DCS_histogram image_histogram = DCS::create_histogram("/home/sbobovyc/DCS_github/DCS3/image.jpeg");
	DCS::DCS_color_list color_list = DCS::calculate_colors(image_histogram, num_colors);
	Color base_color = DCS::calculate_base_color(color_list);

	//DCS::print_histogram(image_histogram);

	for(int i = 0; i < int(color_list.size()); i++)
	{
		cout << "Color " << i << ": " << color_list[i].first.redQuantum() << " " << color_list[i].first.greenQuantum() << " " << color_list[i].first.blueQuantum() << endl;
		DCS::DCS_color color = DCS::MagickColor_to_DCS_Color(color_list[i].first);
		cout << "Color " << i << ": " << color.red << " " << color.green << " " << color.blue << endl;
	}

	cout << "Base color: " << base_color.redQuantum() << " " << base_color.greenQuantum() << " " << base_color.blueQuantum() << endl;
	DCS::DCS_color color = DCS::MagickColor_to_DCS_Color(base_color);
	cout << "Color: " << color.red << " " << color.green << " " << color.blue << endl;

	vector< DCS::DCS_color> DCS_color_list;
	for(int i = 0; i < color_list.size(); i++)
	{
		DCS::DCS_color tmp_color;
		tmp_color.red = color_list[i].first.redQuantum();
		tmp_color.green = color_list[i].first.greenQuantum();
		tmp_color.blue = color_list[i].first.blueQuantum();
		DCS_color_list.push_back(tmp_color);

	}

	vector< Image > image_list;
	image_list.push_back(Image(Geometry(canvas_width, canvas_height), base_color));

	srand(time(NULL));
	for(int i = 1; i < DCS_color_list.size()+1; i++)
	{
		Timer timer;
		timer.start();
		image_list.push_back(Image(Geometry(canvas_width, canvas_height), Color(0,0,0,TransparentOpacity)));
		int seed = rand();
		//sleep(1);
		cout << "Seed " << seed << endl;
		DCS::draw_blobs(DCS_color_list[i-1], canvas_width, canvas_height, octave_count, frequency, persistence, seed, threshold, z, &image_list[i]);
		timer.stop();
		cout << "Run time :" << timer.read() << endl;
	}


	image_list[0].write("/home/sbobovyc/DCS_github/DCS3/out0.png");
	image_list[1].write("/home/sbobovyc/DCS_github/DCS3/out1.png");
	image_list[2].write("/home/sbobovyc/DCS_github/DCS3/out2.png");
//	image_list[3].write("/home/sbobovyc/DCS_github/DCS/DCS3/out3.png");
	Magick::flattenImages(&image_list[0], image_list.begin(), image_list.end());
	image_list[0].write("/home/sbobovyc/DCS_github/DCS3/out.png");
	return 0;
}
