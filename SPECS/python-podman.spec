Name: python-podman
Epoch: 3
Version: 4.4.1
Release: 1%{?dist}
Summary: RESTful API for Podman
License: ASL 2.0
URL: https://github.com/containers/podman-py
Source0: https://github.com/containers/podman-py/archive/refs/tags/v%{version}.tar.gz
BuildArch: noarch

%description
%{name}  is a library of bindings to use the RESTful API for Podman.

%package -n python%{python3_pkgversion}-podman
BuildRequires: git-core
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: pyproject-rpm-macros
Provides: podman-py = %{version}-%{release}
Summary: %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-podman}

%description -n python%{python3_pkgversion}-podman
%{name} is a library of bindings to use the RESTful API for Podman.

%prep
%autosetup -Sgit_am -n podman-py-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}

%build
export PBR_VERSION="0.0.0"
%pyproject_wheel

%install
export PBR_VERSION="0.0.0"
%pyproject_install
%pyproject_save_files podman

%check

%files -n python%{python3_pkgversion}-podman -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Thu Feb 23 2023 Jindrich Novy <jnovy@redhat.com> - 3:4.4.1-1
- update to https://github.com/containers/podman-py/releases/tag/v4.4.1
- Related: #2124478

* Wed Feb 15 2023 Jindrich Novy <jnovy@redhat.com> - 3:4.4.0-1
- update to 4.4.0
- (and revert the unneeded upstream python-tomli dependency)
- Related: #2124478

* Mon Oct 24 2022 Jindrich Novy <jnovy@redhat.com> - 3:4.3.0-1
- update to 4.3.0
- Related: #2124478

* Thu Aug 11 2022 Jindrich Novy <jnovy@redhat.com> - 3:4.2.0-1
- update to https://github.com/containers/podman-py/releases/tag/v4.2.0
- Related: #2061316

* Mon Feb 28 2022 Lokesh Mandvekar <lsm5@redhat.com> - 3:4.0.0-1
- bump to v4.0.0
- Related: #2000051

* Fri Oct 01 2021 Jindrich Novy <jnovy@redhat.com> - 3:3.2.1-3
- perform only sanity/installability tests for now
- Related: #2000051

* Wed Sep 29 2021 Jindrich Novy <jnovy@redhat.com> - 3:3.2.1-2
- rebuilt
- Related: #2000051

* Mon Sep 27 2021 Jindrich Novy <jnovy@redhat.com> - 3:3.2.1-1
- import to c9s
- Related: #2000051
