%define module	Gtk2-ImageView
%define	name	perl-%{module}
%define	version	0.04
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl bindings to the GtkImageView image viewer widget
License:	LGPLv3+
Group:	  	Development/GNOME and GTK+
Source:		http://search.cpan.org/CPAN/authors/id/R/RA/RATCLIFFE/%module-%version.tar.gz
URL:		http://search.cpan.org/Dist/%module
BuildRequires:	perl-Gtk2 >= 1.140
BuildRequires:	perl-ExtUtils-Depends >= 0.2
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.140
BuildRequires:	gtkimageview-devel >= 1.6.0
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Perl bindings to the GtkImageView image viewer widget
Find out more about GtkImageView at http://trac.bjourne.webfactional.com/.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --default
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS README
%{perl_vendorarch}/Gtk2/Gdk/Pixbuf/Draw/Cache.pod
%{perl_vendorarch}/Gtk2/ImageView.pm
%{perl_vendorarch}/Gtk2/ImageView.pod
%{perl_vendorarch}/Gtk2/ImageView
%{perl_vendorarch}/auto/Gtk2/ImageView/ImageView.so
%{_mandir}/man3/*
