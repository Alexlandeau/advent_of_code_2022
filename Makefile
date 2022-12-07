SHELL:=/bin/bash
.SHELLFLAGS += -e
SESSION := $(shell head -n 1 session.txt)

.ONESHELL:
new_day:
	@set -e
	@echo "Starting to build day $(day)..."
	@mkdir day_$(day)
	@curl https://adventofcode.com/2022/day/$(day)/input -o day_$(day)/input.txt --cookie "session=$(SESSION)"
	@touch day_$(day)/day_$(day).py
	@touch day_$(day)/input_example.txt	