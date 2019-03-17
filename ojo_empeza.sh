#!/bin/bash
while true; do
	pic_time=$(date '+%D %X')
	echo "Taking picture at: $pic_time"
	SECONDS=0
	python3 ./ojo_controlador.py
	until [ $SECONDS -gt 3 ]; do
		dummy_variable=true
	done
        echo "Pushing to git at: $(date '+%D %X')"
	git add .
	git commit -a -m "Picture taken at $pic_time"
	git push origin dev
done
