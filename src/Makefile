clean:
	rm -r public/
build:
	hugo --themesDir ../themes
dev: clean
	hugo server --themesDir ../themes
deploy: clean build
	hugo deploy --themesDir ../themes
