Summary:	Tool for editing and converting subtitles for divx films
Summary(pl): 	Program do konwersji napisow do divx'ow
Name:		GTKsubtitler
Version:	v0.1.5
Release:	1
Vendor:	        Pawe³ Boguszewski <pawelb@gower.pl>
License:	GPL
Group:		X11/Applications/Multimedia
Source0:  	http://www.gtksubtitler.prv.pl/download/%{name}-%{version}.tar.gz
Source1:   	GTKsubtitler.desktop
Icon:		GTKsubtitler.xpm
URL:		http://www.gtksubtitler.prv.pl
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root

%description
Tool for editing and converting subtitles 4 divx films. It supports mergeing, 
moveing, changeing format of sub-file and converting (to iso-8859-1/2) divix 
subtitles.

%description -l pl
Program do konwersji napisow do divx'ow. Obsluguje przesuwanie napisów, 
sklejanie dwóch plików (i wiecej) w jeden, zmienianie formatu  i konwersje 
do formatu iso-8859-1/2.


%prep
%setup -q

%build
%configure2_13
%{__make} OPTFLAGS="%{rpmcflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_applnkdir}/Multimedia}
install src/GTKsubtitler $RPM_BUILD_ROOT%{_bindir}/GTKsubtitler
install pixmaps/GTKsubtitler.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/GTKsubtitler.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/%{name}.desktop
%{_pixmapsdir}/GTKsubtitler.xpm
