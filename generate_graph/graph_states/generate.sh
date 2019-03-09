#!/bin/bash

# # Optional Cleanup
# if [[ "$#" = 1 ]]
# then
# 	if [[ "$1" = "rm" ]]
# 	then
# 		`rm g*.png`;
# 		exit(1);
# 	fi
# fi
# Use FFMPEG to generate MP4
ffmpeg -framerate 1 -pattern_type glob -i '*.png'   -c:v libx264 -r 30 -pix_fmt yuv420p graph_vid/recent.mp4
