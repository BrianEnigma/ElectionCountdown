all: push

push:
	rm -rf package
	mkdir package
	cp -r *.html lib img package/
	cd package ; aws --profile=home s3 sync . s3://electioncountdown.org

