clean:
	rm -r public/
build:
	hugo --minify --themesDir ../themes
dev: clean
	hugo server --themesDir ../themes
deploy: build
	hugo deploy --themesDir ../themes
