#!/bin/bash
while true; do
	pic_time=$(date '+%D %X')
	echo "Taking picture at: $pic_time"
	SECONDS=0
        # Call python to take picture and save
	python3 ./ojo_controlador.py
	
        git add .
	git commit -a -m "Picture taken at $pic_time"
	git push origin master
        until [ $SECONDS -gt 300 ]; do
		dummy_variable=true
	done
done
