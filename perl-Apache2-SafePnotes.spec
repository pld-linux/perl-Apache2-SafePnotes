#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	apxs	/usr/sbin/apxs
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache2
%define	pnam	SafePnotes
Summary:	Apache2::SafePnotes - a safer replacement for Apache2::RequestUtil::pnotes
#Summary(pl):	
Name:		perl-Apache2-SafePnotes
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ef1c270b94997042be2300848c0d50d3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-mod_perl
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module cures a problem with Apache2::RequestRec::pnotes and
Apache2::Connection::pnotes (available since mod_perl 2.0.3).
These functions store perl variables making them accessible from
various phases of the Apache request cycle.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

APACHE_TEST_APXS=%{apxs} \
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Apache2/*.pm
%{_mandir}/man3/*
