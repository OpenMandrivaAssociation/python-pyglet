%define module  pyglet
%define name 	python-%{module}
%define version 1.1.4
%define release %mkrel 1

Summary:	A cross-platform windowing and multimedia library for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pyglet.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python >= 2.5
Requires:	libmesagl, libmesaglu, gdk-pixbuf
BuildRequires:	python-devel >= 2.5
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
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE CHANGELOG NOTICE examples/ doc/html/
%py_puresitedir/*


%changelog
* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 1.1.4-1mdv2011.0
+ Revision: 598280
- rebuild for py2.7

* Thu Jan 07 2010 Lev Givon <lev@mandriva.org> 1.1.4-1mdv2010.1
+ Revision: 487371
- Update to 1.1.4.

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1.3-2mdv2010.0
+ Revision: 442418
- rebuild

  + Lev Givon <lev@mandriva.org>
    - Update to 1.1.3.

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.1.2-2mdv2009.1
+ Revision: 323951
- rebuild

* Fri Oct 24 2008 Lev Givon <lev@mandriva.org> 1.1.2-1mdv2009.1
+ Revision: 296980
- Update to 1.1.2.

* Tue Aug 05 2008 Lev Givon <lev@mandriva.org> 1.1-1mdv2009.0
+ Revision: 263985
- Update to 1.1.

* Fri May 09 2008 Lev Givon <lev@mandriva.org> 1.0-1mdv2009.0
+ Revision: 205341
- import python-pyglet


* Fri May 9 2008 Lev Givon <lev@mandriva.org> 1.0-1mdv2008.1
- Package for Mandriva.

