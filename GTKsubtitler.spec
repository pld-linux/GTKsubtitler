# NB:
#  PROJECT CLOSED -- no upstream developments
Summary:	Tool for editing and converting subtitles for DivX films
Summary(pl.UTF-8):	Program do konwersji napisów do filmów w formacie DivX
Name:		GTKsubtitler
Version:	v0.2.4
Release:	3
Vendor:		Paweł Boguszewski <pawelb@pld-linux.org>
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://pawelb.loki-a.com/projects/gtksubtitler/download/%{name}-%{version}.tar.gz
# Source0-md5:	9610878afb2978a2a293f8d5b205673b
Source1:	%{name}.desktop
URL:		http://www.gtksubtitler.prv.pl/
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for editing and converting subtitles for DivX films. It supports
mergeing, moveing, changeing format of sub-file and converting (to
iso-8859-1/2) divix subtitles.

%description -l pl.UTF-8
Program do konwersji napisów do filmów w formacie DivX. Obsługuje
przesuwanie napisów, sklejanie dwóch (i więcej) plików w jeden,
zmienianie formatu i konwersje do formatu iso-8859-1/2.

%prep
%setup -q

%build
%configure2_13
%{__make} \
	OPTFLAGS="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}
install src/GTKsubtitler $RPM_BUILD_ROOT%{_bindir}/GTKsubtitler
install pixmaps/GTKsubtitler.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/GTKsubtitler.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README SUB_FORMATS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/GTKsubtitler.xpm
