/*
 * @file utils.cpp
 *
 * @date Jun 22, 2011
 * @author sbobovyc
 * @description
 */

#include <noise.h>
#include <omp.h>
#include "utils.hpp"

int test(void)
{
	return 10;
}
void draw_blobs(const int canvas_width, const int canvas_height, const int octave_count, const double frequency, const double persistence, const int seed, const double threshold, const double z, int ** mask)
{
	noise::module::Perlin module;
	module.SetOctaveCount(octave_count);
	module.SetFrequency(frequency);
	module.SetPersistence(persistence);
	module.SetSeed(seed);

	//#pragma omp parallel for
	for(int i = 0; i < canvas_width; i++)
	{
		//#pragma omp parallel for
		for(int j = 0; j < canvas_height; j++)
		{
			double value = module.GetValue(i, j, z);
			//cout << i << " " << j << " " << value << endl;
			if(value > threshold)
			{
				mask[i][j] = 1;
			}
		}
	}
}
