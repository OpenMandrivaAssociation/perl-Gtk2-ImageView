%define upstream_name Gtk2-ImageView
%define upstream_version 0.05
Name:		perl-%{upstream_name}
Version:	0.05
Release:	1

Summary:	Perl bindings to the GtkImageView image viewer widget
License:	LGPLv3+
Group:		Development/GNOME and GTK+
Url:		https://metacpan.org/dist/Gtk2-ImageView
Source0:	https://cpan.metacpan.org/authors/id/R/RA/RATCLIFFE/Gtk2-ImageView-0.05.tar.gz
Source100:	perl-Gtk2-ImageView.rpmlintrc
BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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


