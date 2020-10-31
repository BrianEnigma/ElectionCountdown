all: pytz
	rm -rf package
	mkdir package
	cp lambda.py date_countdown.py settings.py package/
	cp -R pytz/* package
	rm -f election_countdown.zip
	cd package ; zip -r ../election_countdown.zip *

pytz:
	pip3 install -t ./pytz pytz

clean:
	rm -rf package

distclean: clean
	rm -rf pytz

