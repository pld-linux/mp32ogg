Summary:	MP3 to Ogg Vorbis converter
Summary(pl.UTF-8):	Konwerter MP3 do Ogg Vorbis
Name:		mp32ogg
Version:	0.11
Release:	2
License:	Artistic
Group:		Applications/Multimedia
Source0:	ftp://ftp.faceprint.com/pub/software/scripts/%{name}
# Source0-md5:	7da7d3b125d2d0a6c12bbb0e9cdb93ff
URL:		http://faceprint.com/code/
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	mpg123
Requires:	vorbis-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A perl script to convert MP3 files to Ogg Vorbis files, retaining ID3
information, bitrate, and optionally renaming the output files, as
well as deleting the originals.

THIS DEGRADES THE QUALITY, because it goes from one lossy format to
another.

%description -l pl.UTF-8
Jest to skrypt Perla konwertujący pliki MP3 na Ogg Vorbis, z
zachowaniem informacji ID3, bitrate i opcjonalnie zmieniający nazwy
plików wyjściowych oraz usuwający pliki oryginalne.

TAKA KONWERSJA OBNIŻA JAKOŚĆ, ponieważ jest to przejście z jednego
stratnego formatu na inny.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

sed "s/$quality = 8;/$quality = 7;/" %{SOURCE0} > $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
