PYTHON = python3
VIEWER = less

.PHONY: run

run :  pairs_inArray_withSum_equalTo_10.py
	python3 pairs_inArray_withSum_equalTo_10.py

time : time.py
	python3 time.py
	gnuplot < plot-instructions
	@echo "done"
	open 2.png

clean :
	rm output.out > /dev/null 2>&1
	rm 2.png > /dev/null 2>&1
	rm -rf __pycache__/ > /dev/null 2>&1
	rm *.pyc > /dev/null 2>&1
