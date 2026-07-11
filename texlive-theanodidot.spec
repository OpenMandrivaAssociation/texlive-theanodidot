%global tl_name theanodidot
%global tl_revision 78931

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	TheanoDidot fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/theanodidot
License:	lppl ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/theanodidot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/theanodidot.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the TheanoDidot font designed by Alexey Kryukov,
in both TrueType and Type1 formats, with support for both traditional
and modern LaTeX processors. An artificially-emboldened variant has been
provided but there are no italic variants. The package is named after
Theano, a famous Ancient Greek woman philosopher, who was first a
student of Pythagoras, and supposedly became his wife. The Didot family
were active as designers for about 100 years in the 18th and 19th
centuries. They were printers, publishers, typeface designers, inventors
and intellectuals. Around 1800 the Didot family owned the most important
print shop and font foundry in France. Pierre Didot, the printer,
published a document with the typefaces of his brother, Firmin Didot,
the typeface designer. The strong clear forms of this alphabet display
objective, rational characteristics and are representative of the time
and philosophy of the Enlightenment.

