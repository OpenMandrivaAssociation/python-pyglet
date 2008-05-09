%define module pyglet
%define name python-%{module}
%define version 1.0
%define release %mkrel 1

Summary: A cross-platform windowing and multimedia library for Python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{module}-%{version}.tar.lzma
License: BSD
Group: Development/Python
Url: http://pyglet.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: python >= 2.5
Requires: libmesagl1, libmesaglu1
BuildRequires: python-devel >= 2.5
BuildArch: noarch

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
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc README LICENSE CHANGELOG NOTICE examples/ doc/*

