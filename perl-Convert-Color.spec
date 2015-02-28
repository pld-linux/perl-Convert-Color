#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Convert
%define		pnam	Color
%include	/usr/lib/rpm/macros.perl
Summary:	Convert::Color - color space conversions and named lookups
Name:		perl-Convert-Color
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Convert/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5d4ec8b804100dca53c6c406f2a83f4c
URL:		http://search.cpan.org/dist/Convert-Color/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(List::UtilsBy)
BuildRequires:	perl-Module-Pluggable
BuildRequires:	perl-Test-Number-Delta
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides conversions between commonly used ways to express
colors. It provides conversions between color spaces such as RGB and
HSV, and it provides ways to look up colors by a name.

This class provides a base for subclasses which represent particular
color values in particular spaces. The base class provides methods to
represent the color in a few convenient forms, though subclasses may
provide more specific details for the space in question.

For more detail, read the documentation on these classes; namely:

The following classes are subclasses of one of the above, which
provide a way to access predefined colors by names:

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Convert/*.pm
%{perl_vendorlib}/Convert/Color
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
