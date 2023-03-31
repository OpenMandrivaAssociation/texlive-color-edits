Name:		texlive-color-edits
Version:	56707
Release:	2
Summary:	Colorful edits for multiple authors of a shared document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/color-edits
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/color-edits.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/color-edits.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/color-edits.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a fairly light-weight solution for
annotating LaTeX source code with color to show
additions/changes, replacements, deletions, and comments. This
is particularly useful when a document is being edited by
multiple authors. Two package options allow the quick
suppression of all colorful edits and comments, and showing
text whose deletion was proposed.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/color-edits
%{_texmfdistdir}/tex/latex/color-edits
%doc %{_texmfdistdir}/doc/latex/color-edits

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
