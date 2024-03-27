Name     : imv
Version  : 4.5.0
Release  : 1
URL       : https://sr.ht/~exec64/imv/
Source0  : https://git.sr.ht/~exec64/imv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary  : image viewer
Group    : Development/Tools
License  : MIT
BuildRequires : meson
BuildRequires : asciidoc
BuildRequires : libpng-dev
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libturbojpeg)
BuildRequires : pkgconfig(cmocka)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(icu-io)
BuildRequires : pkgconfig(inih)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(glu)
#BuildRequires : pkgconfig(x11)
#BuildRequires : pkgconfig(xcb)
#BuildRequires : pkgconfig(xkbcommon-x11)
#BuildRequires : freeimage-dev


%description
image viewer


%prep
%setup -q -n imv-v%{version}


%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Ofast -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -Ofast -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -Ofast -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" FCFLAGS="$FFLAGS" meson -Dlibheif=disabled -Dlibnsgif=disabled -Dlibtiff=disabled  --libdir=lib64 --prefix=/usr --buildtype=plain  builddir
ninja -v -C builddir


%install
DESTDIR=%{buildroot} ninja -C builddir install
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/imv
/usr/bin/imv-wayland
/usr/bin/imv-msg
/usr/bin/imv-x11
/usr/share/applications/imv.desktop
/usr/bin/imv-dir
/usr/share/applications/imv-dir.desktop
