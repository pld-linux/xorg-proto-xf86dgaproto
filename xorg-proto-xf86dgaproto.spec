# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	XF86DGA extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia XF86DGA
Name:		xorg-proto-xf86dgaproto
Version:	2.1
Release:	3.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/xf86dgaproto-%{version}.tar.bz2
# Source0-md5:	a036dc2fcbf052ec10621fd48b68dbb1
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86DGA extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia XF86DGA.

%package devel
Summary:	XF86DGA extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia XF86DGA
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
XF86DGA extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia XF86DGA.

%prep
%setup -q -n xf86dgaproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/xf86dga*.h
%{_pkgconfigdir}/xf86dgaproto.pc
