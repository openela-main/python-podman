Name: python-podman
Version: 4.0.0
Release: 2%{?dist}
Summary: RESTful API for Podman
License: ASL 2.0
URL: https://github.com/containers/podman-py
Source0: %{url}/releases/download/v%{version}/podman-%{version}.tar.gz
BuildArch: noarch

%description
%{name} is a library of bindings to use the RESTful API for Podman.

%package -n python%{python3_pkgversion}-podman
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: python%{python3_pkgversion}-toml
Requires: python%{python3_pkgversion}-toml
%else
BuildRequires: python%{python3_pkgversion}-pytoml
Requires: python%{python3_pkgversion}-pytoml
%endif
BuildRequires: python%{python3_pkgversion}-pyxdg
BuildRequires: python%{python3_pkgversion}-requests
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: git-core
Requires: python%{python3_pkgversion}-pyxdg
Requires: python%{python3_pkgversion}-requests
Provides: podman-py = %{version}-%{release}
Summary: %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-podman}

%description -n python%{python3_pkgversion}-podman
%{name} is a library of bindings to use the RESTful API for Podman.

%prep
%autosetup -Sgit_am -n podman-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-podman
%license LICENSE
%doc README.md
%{python3_sitelib}/podman/*
%{python3_sitelib}/podman-*/*

%changelog
* Tue Mar 14 2023 Jindrich Novy <jnovy@redhat.com> - 4.0.0-2
- bump to v4.0.0
- Related: #2176055

* Mon Feb 28 2022 Lokesh Mandvekar <lsm5@redhat.com> - 4.0.0-1
- bump to v4.0.0
- Related: #2001445

* Wed Sep 29 2021 Jindrich Novy <jnovy@redhat.com> - 3.2.1-4
- do not depend on pyproject-rpm-macros - not present in RHEL8
- Related: #2001445

* Wed Jul 28 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 3.2.0-2
- depend on python3-requests
- Resolves: #1978415 - initial upload to rhel

* Wed Jul 28 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 3.2.0-1
- Bump to v3.2.0

* Tue May 04 2021 Lokesh Mandvekar <lsm5@fedoraproject.org> - 3.1.2.4-1
- Initial package

