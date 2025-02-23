Name:		texlive-sepnum
Version:	20186
Release:	2
Summary:	Print numbers in a "friendly" format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sepnum
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sepnum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sepnum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a command to print a number with (potentially
different) separators every three digits in the parts either
side of the decimal point (the point itself is also
configurable). The macro is fully expandable and not fragile
(unless one of the separators is). There is also a command
\sepnumform, that may be used when defining \the<counter>
macros.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sepnum/sepnum.sty
%doc %{_texmfdistdir}/doc/latex/sepnum/sepnum-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sepnum/sepnum-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
