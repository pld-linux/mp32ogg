%include	/usr/lib/rpm/macros.perl
Summary:	mp3 to ogg vorbis converter
Summary(pl):	Konwerter mp3 do ogg vorbis
Name:		mp32ogg
Version:	0.11
Release:	1
License:	Artistic
Group:		Applications/Multimedia
Source0:	ftp://ftp.faceprint.com/pub/software/scripts/%{name}
URL:		http://faceprint.com/code/
Requires:	vorbis-tools
Requires:	mpg123
BuildRequires:	perl >= 5.6
BuildRequires:	perl-modules
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A perl script to convert MP3 files to Ogg Vorbis files, retaining ID3
information, bitrate, and optionally renaming the output files, as
well as deleting the originals.

THIS DEGRADES THE QUALITY, because it goes from one lossy format to
another.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
