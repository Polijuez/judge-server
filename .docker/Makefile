GIT_TAG ?= master
TAG ?= latest

DOCKER_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
REPO_ROOT := $(abspath $(DOCKER_DIR)/..)

.PHONY: all judge-tier1 judge-tier2 judge-tier3

all: judge-tier1 judge-tier2 judge-tier3

judge-tier1:
	cd tier1 && docker build --build-arg TAG="${GIT_TAG}" -t dmoj/judge-tier1 -t dmoj/judge-tier1:$(TAG) .

judge-tier2:
	cd tier2 && docker build --build-arg TAG="${GIT_TAG}" -t dmoj/judge-tier2 -t dmoj/judge-tier2:$(TAG) .

judge-tier3:
	docker build -f "$(DOCKER_DIR)/tier3/Dockerfile" -t dmoj/judge-tier3 -t dmoj/judge-tier3:$(TAG) "$(REPO_ROOT)"
