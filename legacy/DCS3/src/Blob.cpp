/*
 * Blob.cpp
 *
 *  Created on: May 31, 2011
 *      Author: sbobovyc
 */

#include "Blob.hpp"
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <vector>
#include <iostream>

using namespace std;

namespace DCS {

DCS_Blob::DCS_Blob(vector<int> _color, int _width, int _height, int _canvas_width, int _canvas_height, int _max_level, pair<int,int> _seed_coords, int _distribution[8])
{
	color = _color;
	height = _height;
	width = _width;
	canvas_height = _canvas_height;
	canvas_width = _canvas_width;
	current_level = 0;
	max_level = _max_level;
	seed_coords = _seed_coords;
	memcpy(distribution, _distribution, 8*sizeof(int));
	regression = {100/max_level, 100/max_level, 100/max_level, 100/max_level, 100/max_level, 100/max_level, 100/max_level, 100/max_level};
	Build(current_level, seed_coords);
}

/**
 * Recursive function for blob construction.
 * @param current_level
 * @param coordinates
 */
void DCS_Blob::Build(int current_level, pair<int,int> coordinates) {
    if(current_level == 0)
	{
    	rectangle_list.push_back( pair<pair<int,int>,pair<int,int> > (pair<int,int> (coordinates.first, coordinates.second) , pair<int,int> (coordinates.first+width, coordinates.second+height)) );

        if (Random() < distribution[0])
            Build(current_level+1, pair<int,int> (coordinates.first-width, coordinates.second-height));
        if (Random() < distribution[1])
        	Build(current_level+1, pair<int,int> (coordinates.first, coordinates.second-height));
        if (Random() < distribution[2])
			Build(current_level+1, pair<int,int> (coordinates.first+width, coordinates.second-height));
        if (Random() < distribution[3])
        	Build(current_level+1, pair<int,int> (coordinates.first-width, coordinates.second));
        if (Random() < distribution[4])
        	Build(current_level+1, pair<int,int> (coordinates.first+width, coordinates.second));
        if (Random() < distribution[5])
        	Build(current_level+1, pair<int,int> (coordinates.first-width, coordinates.second+height));
        if (Random() < distribution[6])
			Build(current_level+1, pair<int,int> (coordinates.first, coordinates.second+height));
        if (Random() < distribution[7])
			Build(current_level+1, pair<int,int> (coordinates.first+width, coordinates.second+height));
	}
    else if(current_level <= max_level){
    	rectangle_list.push_back( pair<pair<int,int>,pair<int,int> > (pair<int,int> (coordinates.first, coordinates.second) , pair<int,int> (coordinates.first+width, coordinates.second+height)) );

    	// distribution is reduntantly calculated, but this is an easy way to implement
    	int tmp_distribution[8] = {0,0,0,0,0,0,0,0};
    	for(int i = 0; i < 8; i++)
    		tmp_distribution[i] = distribution[i] - regression[i]*current_level;

        if (Random() < tmp_distribution[0])
            Build(current_level+1, pair<int,int> (coordinates.first-width, coordinates.second-height));
        if (Random() < tmp_distribution[1])
        	Build(current_level+1, pair<int,int> (coordinates.first, coordinates.second-height));
        if (Random() < tmp_distribution[2])
			Build(current_level+1, pair<int,int> (coordinates.first+width, coordinates.second-height));
        if (Random() < tmp_distribution[3])
        	Build(current_level+1, pair<int,int> (coordinates.first-width, coordinates.second));
        if (Random() < tmp_distribution[4])
        	Build(current_level+1, pair<int,int> (coordinates.first+width, coordinates.second));
        if (Random() < tmp_distribution[5])
        	Build(current_level+1, pair<int,int> (coordinates.first-width, coordinates.second+height));
        if (Random() < tmp_distribution[6])
			Build(current_level+1, pair<int,int> (coordinates.first, coordinates.second+height));
        if (Random() < tmp_distribution[7])
			Build(current_level+1, pair<int,int> (coordinates.first+width, coordinates.second+height));
	}
}

/**
 * @return random number ranging 1 to 100
 */
int DCS_Blob::Random()
{
	/* initialize random seed: */
	srand(time(NULL));
	return rand() % 100 + 1;
}

std::ostream & operator<<(ostream &out, DCS_Blob const & blob)     //output
{
		for(unsigned int i = 0; i < blob.rectangle_list.size(); i++)
		{
			out << "(" << blob.rectangle_list[i].first.first << "," << blob.rectangle_list[i].first.second << ")" << " " <<
					"(" << blob.rectangle_list[i].second.first << "," << blob.rectangle_list[i].second.second << ")" <<
					endl;
		}
        return out;
}

std::vector< std::pair< std::pair<int,int>, std::pair<int,int> > > DCS_Blob::get_rectangle_list()
{
	return rectangle_list;
}

DCS_Blob::~DCS_Blob() {
	// TODO Auto-generated destructor stub
}
}
