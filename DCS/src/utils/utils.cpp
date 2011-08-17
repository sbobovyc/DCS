/*
 * @file utils.cpp
 *
 * @date Jun 22, 2011
 * @author sbobovyc
 * @description
 */
/*
    Copyright (C) 2011 Stanislav Bobovych

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

 */

#include <libnoise/noise.h>
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
	for(int i = 0; i < canvas_height; i++)
	{
		//#pragma omp parallel for
		for(int j = 0; j < canvas_width; j++)
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
