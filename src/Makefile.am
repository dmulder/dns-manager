
python_PYTHON = libyui.py

dnslibdir = $(pythondir)/dnsmanager
dnslib_DATA = include/*

yui_ext_wrap.cxx: yui_ext.i yui_ext.h
	$(SWIG) $(AX_SWIG_PYTHON_OPT) -c++ -I/usr/include/yui $(CPPFLAGS) -o $@ $<

SWIG_SOURCES = yui_ext.i

pkgpython_PYTHON = yui_ext.py
pkgpyexec_LTLIBRARIES = _yui_ext.la
_yui_ext_la_SOURCES = yui_ext_wrap.cxx yui_ext.cpp
_yui_ext_la_CPPFLAGS = -I/usr/include/yui $(SWIG_PYTHON_CPPFLAGS) `${PYTHON}-config --cflags`
_yui_ext_la_LDFLAGS = -module
_yui_ext_la_LIBADD = -lyui

CLEANFILES = yui_ext_wrap.cxx yui_ext.py
