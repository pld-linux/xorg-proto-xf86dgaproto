Summary:	XF86DGA protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XF86DGA i pomocnicze
Name:		xorg-proto-xf86dgaproto
Version:	2.0.2
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/proto/xf86dgaproto-%{version}.tar.bz2
# Source0-md5:	461aa291a23e8cf387b70f3efa71b05c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XF86DGA protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u XF86DGA i pomocnicze.

%package devel
Summary:	XF86DGA protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XF86DGA i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
XF86DGA protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u XF86DGA i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xf86dgaproto.pc
