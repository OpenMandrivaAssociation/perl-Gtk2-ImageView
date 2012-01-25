%define upstream_name	 Gtk2-ImageView
%define	upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl bindings to the GtkImageView image viewer widget
License:	LGPLv3+
Group:	  	Development/GNOME and GTK+
Url:		http://search.cpan.org/Dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/R/RA/RATCLIFFE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Gtk2 >= 1.140
BuildRequires:	perl-ExtUtils-Depends >= 0.2
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.140
BuildRequires:	gtkimageview-devel >= 1.6.0
BuildRequires:	perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Perl bindings to the GtkImageView image viewer widget
Find out more about GtkImageView at http://trac.bjourne.webfactional.com/.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
