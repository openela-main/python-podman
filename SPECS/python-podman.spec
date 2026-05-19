# RHEL 8 envs has slightly different python deps
# and also doesn't support dynamic (build)requires.
%if %{defined rhel} && 0%{?rhel} == 8
%define rhel8_py 1
%endif

%global pypi_name podman
%global desc %{pypi_name} is a library of bindings to use the RESTful API for Podman.

%global pypi_dist 4

Name: python-%{pypi_name}
%if %{defined copr_username}
Epoch: 102
%else
Epoch: 3
%endif
# DO NOT TOUCH the Version string!
# The TRUE source of this specfile is:
# https://github.com/containers/podman/blob/main/rpm/python-podman.spec
# If that's what you're reading, Version must be 0, and will be updated by Packit for
# copr and koji builds.
# If you're reading this on dist-git, the version is automatically filled in by Packit.
Version: 5.7.0
Release: 1%{?dist}
License: Apache-2.0
Summary: RESTful API for Podman
URL: https://github.com/containers/%{pypi_name}-py
# Tarball fetched from upstream
Source0: %{url}/archive/v%{version}.tar.gz
BuildArch: noarch

%description
%desc

%package -n python%{python3_pkgversion}-%{pypi_name}
BuildRequires: git-core
BuildRequires: python%{python3_pkgversion}-devel
%if %{defined rhel8_py}
BuildRequires: python%{python3_pkgversion}-rpm-macros
BuildRequires: python%{python3_pkgversion}-pytoml
BuildRequires: python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-pytoml
Requires: python%{python3_pkgversion}-requests
%else
BuildRequires: pyproject-rpm-macros
%endif
Provides: %{pypi_name}-py = %{epoch}:%{version}-%{release}
Provides: python%{python3_pkgversion}dist(%{pypi_name}) = %{pypi_dist}
Provides: python%{python3_version}dist(%{pypi_name}) = %{pypi_dist}
Obsoletes: python%{python3_pkgversion}-%{pypi_name}-api <= 0.0.0-1
Provides: python%{python3_pkgversion}-%{pypi_name}-api = %{epoch}:%{version}-%{release}
Summary: %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
%desc

%prep
%autosetup -Sgit -n %{pypi_name}-py-%{version}

%if !%{defined rhel8_py}
%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}
%endif

%build
export PBR_VERSION="0.0.0"
%if %{defined rhel8_py}
%py3_build
%else
%pyproject_wheel
%endif

%install
export PBR_VERSION="0.0.0"
%if %{defined rhel8_py}
%py3_install
%else
%pyproject_install
%pyproject_save_files %{pypi_name}
%endif

%check

%if %{defined rhel8_py}
%files -n python%{python3_pkgversion}-%{pypi_name}
%dir %{python3_sitelib}/%{pypi_name}-*-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}-*-py%{python3_version}.egg-info/*
%dir %{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}/*
%else
%pyproject_extras_subpkg -n python%{python3_pkgversion}-%{pypi_name} progress_bar
%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%endif
%license LICENSE
%doc README.md

%changelog
* Wed Feb 04 2026 Jindrich Novy <jnovy@redhat.com> - 3:5.7.0-1
- update to https://github.com/containers/podman-py/releases/tag/v5.7.0
- Related: RHEL-111919

* Tue Sep 16 2025 Jindrich Novy <jnovy@redhat.com> - 3:5.6.0-1
- update to https://github.com/containers/podman-py/releases/tag/v5.6.0
- Related: RHEL-111919

* Fri Jun 20 2025 Jindrich Novy <jnovy@redhat.com> - 3:5.5.0-1
- update to https://github.com/containers/podman-py/releases/tag/v5.5.0
- Related: RHEL-80816

* Mon Mar 03 2025 Jindrich Novy <jnovy@redhat.com> - 3:5.4.0.1-1
- update to https://github.com/containers/podman-py/releases/tag/v5.4.0.1
- Resolves: RHEL-81952

* Wed Nov 27 2024 Jindrich Novy <jnovy@redhat.com> - 3:5.3.0-1
- update to https://github.com/containers/podman-py/releases/tag/v5.3.0
- Resolves: RHEL-69140

* Mon Aug 05 2024 Jindrich Novy <jnovy@redhat.com> - 3:5.2.0-1
- update to https://github.com/containers/podman-py/releases/tag/v5.2.0
- Related: RHEL-27608

* Mon Mar 25 2024 Jindrich Novy <jnovy@redhat.com> - 3:5.0.0-1
- update to https://github.com/containers/podman-py/releases/tag/v5.0.0
- Resolves: RHEL-30257

* Tue Jan 23 2024 Jindrich Novy <jnovy@redhat.com> - 3:4.9.0-1
- update to https://github.com/containers/podman-py/releases/tag/v4.9.0
- Related: RHEL-2112

* Fri Jan 05 2024 Jindrich Novy <jnovy@redhat.com> - 3:4.8.2-1
- update to https://github.com/containers/podman-py/releases/tag/v4.8.2
- Related: RHEL-2112

* Tue Jan 02 2024 Jindrich Novy <jnovy@redhat.com> - 3:4.8.1-1
- update to https://github.com/containers/podman-py/releases/tag/v4.8.1
- Related: RHEL-2112

* Wed Dec 06 2023 Lokesh Mandvekar <lsm5@redhat.com> - 3:4.8.0.post1-1
- update to https://github.com/containers/podman-py/releases/tag/v4.8.0.post1
- Related: Jira:RHEL-2112

* Fri Sep 29 2023 Jindrich Novy <jnovy@redhat.com> - 3:4.7.0-1
- update to https://github.com/containers/podman-py/releases/tag/v4.7.0
- Related: Jira:RHEL-2112

* Thu Jul 27 2023 Jindrich Novy <jnovy@redhat.com> - 3:4.6.0-1
- update to https://github.com/containers/podman-py/releases/tag/v4.6.0
- Related: #2176063

* Fri Jun 02 2023 Jindrich Novy <jnovy@redhat.com> - 3:4.5.1-1
- update to https://github.com/containers/podman-py/releases/tag/v4.5.1
- Related: #2176063

* Tue May 02 2023 Jindrich Novy <jnovy@redhat.com> - 3:4.5.0-1
- update to https://github.com/containers/podman-py/releases/tag/v4.5.0
- Related: #2176063

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
