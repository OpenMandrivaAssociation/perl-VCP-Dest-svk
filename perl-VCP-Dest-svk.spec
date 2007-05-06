%define realname  VCP-Dest-svk

Name:		perl-%{realname}
Version:	0.29
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:    VCP driver to write svk repository
Source0:    http://www.cpan.org/authors/id/C/CL/CLKAO/%{realname}-%{version}.tar.bz2
Url:		http://searc.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel perl-IPC-Run3 perl-BFD 
BuildRequires:	perl-VCP perl-SVK
BuildArch:      noarch
%description
This driver allows vcp to insert revisions in to a Subversion repository via 
the svk interface. You could use the vcp command line interface or the 
integrated SVK mirror command.

Among other it allows you to mirror cvs repository with the svk command. 

Check http://svk.elixus.org/?SVKCVS and http://svk.elixus.org/?MirrorVCP for
more information.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
# (misc) parallel build broken
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README 
%{perl_vendorlib}/*
%{_mandir}/man3/*

