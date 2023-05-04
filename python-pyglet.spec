%define module  pyglet

Summary:	A cross-platform windowing and multimedia library for Python
Name:		python-%{module}
Version:	2.0.6
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pyglet/%{module}-%{version}.zip
License:	BSD
Group:		Development/Python
Url:		http://pyglet.org
Requires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Pyglet provides an object-oriented programming interface for
developing games and other visually-rich applications for Windows, Mac
OS X and Linux. Some of the features of pyglet are:

* No external dependencies or installation requirements. For most
  application and game requirements, pyglet needs nothing else besides
  Python, simplifying distribution and installation.

* Take advantage of multiple windows and multi-monitor
  desktops. pyglet allows you to use as many windows as you need,
  and is fully aware of multi-monitor setups for use with
  fullscreen games.

* Load images, sound, music and video in almost any format. pyglet can
  optionally use AVbin to play back audio formats such as MP3,
  OGG/Vorbis and WMA, and video formats such as DivX, MPEG-2, H.264,
  WMV and Xvid.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
python setup.py build

%install
python setup.py install --root %{buildroot}

%files
%defattr(-,root,root)
%py_puresitedir/*
