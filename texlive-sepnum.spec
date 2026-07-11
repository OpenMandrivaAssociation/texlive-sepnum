%global tl_name sepnum
%global tl_revision 20186

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Print numbers in a friendly format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sepnum
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sepnum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sepnum.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides a command to print a number with (potentially different)
separators every three digits in the parts either side of the decimal
point (the point itself is also configurable). The macro is fully
expandable and not fragile (unless one of the separators is). There is
also a command \sepnumform, that may be used when defining \the<counter>
macros.

