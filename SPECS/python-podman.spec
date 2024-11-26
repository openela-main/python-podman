%global import_path github.com/containers/podman-py
%global branch release-4.9
%global commit0 07e1b45ca48db63ae4a3106ee630d120bdd89866
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: python-podman
Version: 4.9.0
Release: 3%{?dist}
Summary: RESTful API for Podman
License: ASL 2.0
URL: https://github.com/containers/podman-py
%if 0%{?branch:1}
Source0: https://%{import_path}/tarball/%{commit0}/%{branch}-%{shortcommit0}.tar.gz
%else
Source0: https://%{import_path}/archive/%{commit0}/%{name}-%{version}-%{shortcommit0}.tar.gz
%endif
BuildArch: noarch

%description
%{name} is a library of bindings to use the RESTful API for Podman.

%package -n python%{python3_pkgversion}-podman
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}-pytoml
BuildRequires: python%{python3_pkgversion}-pyxdg
BuildRequires: python%{python3_pkgversion}-requests
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: git-core
BuildRequires: python%{python3_pkgversion}-sphinx
Requires: python%{python3_pkgversion}-pytoml
Requires: python%{python3_pkgversion}-pyxdg
Requires: python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-urllib3
Provides: podman-py = %{version}-%{release}
Summary: %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-podman}

%description -n python%{python3_pkgversion}-podman
%{name} is a library of bindings to use the RESTful API for Podman.

%prep
%if 0%{?branch:1}
%autosetup -Sgit -n containers-podman-py-%{shortcommit0}
%else
%autosetup -Sgit -n podman-py-%{commit0}
%endif

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
* Tue Oct 29 2024 Jindrich Novy <jnovy@redhat.com> - 4.9.0-3
- sync with release-4.9 branch
- Resolves: RHEL-31069

* Tue Jul 09 2024 Jindrich Novy <jnovy@redhat.com> - 4.9.0-2
- depend directly on urllib3
- Resolves: RHEL-43567

* Tue Jan 23 2024 Jindrich Novy <jnovy@redhat.com> - 4.9.0-1
- update to https://github.com/containers/podman-py/releases/tag/v4.9.0
- Related: Jira:RHEL-2110

* Fri Jan 05 2024 Jindrich Novy <jnovy@redhat.com> - 4.8.2-1
- update to https://github.com/containers/podman-py/releases/tag/v4.8.2
- Related: Jira:RHEL-2110

* Thu Dec 07 2023 Lokesh Mandvekar <lsm5@redhat.com> - 4.8.0.post1-1
- update to https://github.com/containers/podman-py/releases/tag/v4.8.0.post1
- Related: Jira:RHEL-2110

* Fri Sep 29 2023 Jindrich Novy <jnovy@redhat.com> - 4.7.0-1
- update to https://github.com/containers/podman-py/releases/tag/v4.7.0
- Related: Jira:RHEL-2110

* Thu Jul 27 2023 Jindrich Novy <jnovy@redhat.com> - 4.6.0-1
- update to https://github.com/containers/podman-py/releases/tag/v4.6.0
- Related: #2176055

* Tue Jun 06 2023 Jindrich Novy <jnovy@redhat.com> - 4.5.1-1
- update to https://github.com/containers/podman-py/releases/tag/v4.5.1
- Related: #2176055

* Thu May 11 2023 Jindrich Novy <jnovy@redhat.com> - 4.5.0-1
- update to https://github.com/containers/podman-py/releases/tag/v4.5.0
- Related: #2176055

* Thu Mar 09 2023 Jindrich Novy <jnovy@redhat.com> - 4.4.1-1
- update to https://github.com/containers/podman-py/releases/tag/v4.4.1
- Related: #2176055

* Mon Nov 07 2022 Jindrich Novy <jnovy@redhat.com> - 4.3.0-2
- upload new source tarball
- Related: #2123641

* Fri Oct 21 2022 Jindrich Novy <jnovy@redhat.com> - 4.3.0-1
- update to https://github.com/containers/podman-py/releases/tag/v4.3.0
- Related: #2123641

* Thu Aug 11 2022 Jindrich Novy <jnovy@redhat.com> - 4.2.0-1
- update to https://github.com/containers/podman-py/releases/tag/v4.2.0
- Related: #2061390

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

