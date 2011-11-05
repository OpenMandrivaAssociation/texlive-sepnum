# revision 20186
# category Package
# catalog-ctan /macros/latex/contrib/sepnum
# catalog-date 2010-10-24 14:34:20 +0200
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-sepnum
Version:	2.0
Release:	1
Summary:	Print numbers in a "friendly" format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sepnum
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sepnum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sepnum.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides a command to print a number with (potentially
different) separators every three digits in the parts either
side of the decimal point (the point itself is also
configurable). The macro is fully expandable and not fragile
(unless one of the separators is). There is also a command
\sepnumform, that may be used when defining \the<counter>
macros.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sepnum/sepnum.sty
%doc %{_texmfdistdir}/doc/latex/sepnum/sepnum-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sepnum/sepnum-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
