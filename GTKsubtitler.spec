Summary:	Tool for editing and converting subtitles for DivX films
Summary(pl):	Program do konwersji napisów do filmów w formacie DivX
Name:		GTKsubtitler
Version:	v0.2.0
Release:	1
Vendor:		Pawe³ Boguszewski <pawelb@gower.pl>
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.gtksubtitler.prv.pl/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Icon:		GTKsubtitler.xpm
URL:		http://www.gtksubtitler.prv.pl/
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for editing and converting subtitles for DivX films. It supports
mergeing, moveing, changeing format of sub-file and converting (to
iso-8859-1/2) divix subtitles.

%description -l pl
Program do konwersji napisów do filmów w formacie DivX. Obs³uguje
przesuwanie napisów, sklejanie dwóch (i wiêcej) plików w jeden,
zmienianie formatu i konwersje do formatu iso-8859-1/2.

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
%doc AUTHORS README SUB_FORMATS
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/%{name}.desktop
%{_pixmapsdir}/GTKsubtitler.xpm
