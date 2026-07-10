%global tl_name color-edits
%global tl_revision 79607

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Colorful edits for multiple authors of a shared document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/color-edits
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/color-edits.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/color-edits.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/color-edits.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a fairly light-weight solution for annotating
LaTeX source code with color to show additions/changes, replacements,
deletions, and comments. This is particularly useful when a document is
being edited by multiple authors. Package options allow the quick
suppression of all colorful edits and comments, hiding edits by some/all
authors, and showing text the deletion of which was proposed.

