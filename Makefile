TARGET_DIR = ../sphinx-contrib/makedomain

sphinxcontrib-release:
	[ ! -e $(TARGET_DIR) ] && mkdir -p $(TARGET_DIR)
	cp -r `ls | grep -v Makefile` $(TARGET_DIR)
	