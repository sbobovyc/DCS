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

//TODO Add boost's command line parsing capabilities
int main(int argc, char ** argv)
{
	int num_colors = 3;
	int canvas_height = 800;
	int canvas_width = 800;
	int octave_count = 2;
	double frequency = 0.02;
	double persistence = 0.1;
	double threshold = 0.1;
	double z = 0.3;


	DCS::DCS_histogram image_histogram = DCS::create_histogram("/home/sbobovyc/DCS_github/DCS3/image.jpeg");
	DCS::DCS_color_vector camo_colors = DCS::calculate_colors(image_histogram, num_colors);
	//DCS::sort_color_vector(camo_colors);
	Magick::Color base_color = DCS::calculate_base_color(camo_colors);

//	DCS::print_histogram(image_histogram);

//	DCS::print_color_vector(camo_colors);

	vector< Magick::Image > image_list;
	image_list.push_back(Magick::Image(Magick::Geometry(canvas_width, canvas_height), base_color));

	srand(time(NULL));
	for(unsigned int i = 1; i < camo_colors.size()+1; i++)
	{
//		DCS::Timer timer;
//		timer.start();
		image_list.push_back( Magick::Image(Magick::Geometry(canvas_width, canvas_height), Magick::Color(0,0,0, TransparentOpacity)) );
		int seed = rand();
		cout << "Seed " << seed << endl;
		DCS::draw_blobs(camo_colors[i-1].first, canvas_width, canvas_height, octave_count, frequency, persistence, seed, threshold, z, &image_list[i]);
//		timer.stop();
//		cout << "Run time :" << timer.read() << endl;
	}

	// 1
//	Magick::Image final_image;
//	Magick::flattenImages(&final_image, image_list.begin(), image_list.end());

	// 2
	Magick::Image final_image(Magick::Geometry(canvas_width, canvas_height), Magick::Color(0,0,0, TransparentOpacity));
	DCS::draw_multi_blobs(camo_colors, 800,800, &final_image);

	// 3
//	Magick::Image final_image(Magick::Geometry(canvas_width, canvas_height), base_color);
//	int seed = 2;
//	noise::module::Perlin module;
//	module.SetOctaveCount(octave_count);
//	module.SetFrequency(frequency);
//	module.SetPersistence(persistence);
//	module.SetSeed(seed);


	final_image.write("/home/sbobovyc/DCS_github/DCS3/out.png");
	return 0;
}
