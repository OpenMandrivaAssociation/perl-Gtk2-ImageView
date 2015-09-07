%define upstream_name Gtk2-ImageView
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl bindings to the GtkImageView image viewer widget
License:	LGPLv3+
Group:		Development/GNOME and GTK+
Url:		http://search.cpan.org/Dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RA/RATCLIFFE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Gtk2 >= 1.140
BuildRequires:	perl-ExtUtils-Depends >= 0.2
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.140
BuildRequires:	gtkimageview-devel >= 1.6.0
BuildRequires:	perl-devel

%description
Perl bindings to the GtkImageView image viewer widget
Find out more about GtkImageView at http://trac.bjourne.webfactional.com/.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --default
%make

%install
%makeinstall_std

%files
%doc AUTHORS README
%{perl_vendorarch}/Gtk2/Gdk/Pixbuf/Draw/Cache.pod
%{perl_vendorarch}/Gtk2/ImageView.pm
%{perl_vendorarch}/Gtk2/ImageView.pod
%{perl_vendorarch}/Gtk2/ImageView
%{perl_vendorarch}/auto/Gtk2/ImageView/ImageView.so
%{_mandir}/man3/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 403230
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2010.0
+ Revision: 370128
- update to new version 0.05

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.04-2mdv2009.0
+ Revision: 268519
- rebuild early 2009.0 package (before pixel changes)

* Sat May 17 2008 Funda Wang <fwang@mandriva.org> 0.04-1mdv2009.0
+ Revision: 208532
- BR perl-devel
- fix file list
- Import source and spec
- Created package structure for perl-Gtk2-ImageView.

