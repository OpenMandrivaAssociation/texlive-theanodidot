Name:		texlive-theanodidot
Version:	64518
Release:	1
Summary:	TheanoDidot fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/theanodidot
License:	lppl ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theanodidot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/theanodidot.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the TheanoDidot font designed by Alexey
Kryukov, in both TrueType and Type1 formats, with support for
both traditional and modern LaTeX processors. An
artificially-emboldened variant has been provided but there are
no italic variants. The package is named after Theano, a famous
Ancient Greek woman philosopher, who was first a student of
Pythagoras, and supposedly became his wife. The Didot family
were active as designers for about 100 years in the 18th and
19th centuries. They were printers, publishers, typeface
designers, inventors and intellectuals. Around 1800 the Didot
family owned the most important print shop and font foundry in
France. Pierre Didot, the printer, published a document with
the typefaces of his brother, Firmin Didot, the typeface
designer. The strong clear forms of this alphabet display
objective, rational characteristics and are representative of
the time and philosophy of the Enlightenment.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/theanodidot
%{_texmfdistdir}/fonts/vf/public/theanodidot
%{_texmfdistdir}/fonts/type1/public/theanodidot
%{_texmfdistdir}/fonts/truetype/public/theanodidot
%{_texmfdistdir}/fonts/tfm/public/theanodidot
%{_texmfdistdir}/fonts/map/dvips/theanodidot
%{_texmfdistdir}/fonts/enc/dvips/theanodidot
%doc %{_texmfdistdir}/doc/fonts/theanodidot

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
