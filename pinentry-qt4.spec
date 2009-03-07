#
# TODO:
# - build with system assuan
#
Summary:	Simple PIN or passphrase entry dialog for Qt
Name:		pinentry-qt4
Version:	0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/unstable/snapshots/kdeplayground-pim-934819.tar.bz2
# Source0-md5:	56cfb1b7a391001ae2e0c59501e1070f
BuildRequires:	QtGui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple PIN or passphrase entry dialog for Qt.

%description -l pl.UTF-8
Prosta kontrolka dialogowa do wpisywania PIN-ów lub haseł dla Qt.

%prep
%setup -q -n kdeplayground-pim-934819

%build
cd pinentry-qt4

install -d build
cd build
%cmake \
		-DCMAKE_INSTALL_PREFIX=%{_prefix} \
		-DLIB_INSTALL_DIR=%{_libdir} \
		-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
		-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
		-DKDE_DISTRIBUTION_TEXT="PLD-Linux" \
%if "%{_lib}" == "lib64"
		-DLIB_SUFFIX=64 \
%endif
		../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C pinentry-qt4/build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pinentry-qt4
