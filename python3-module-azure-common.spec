%define pypi_name azure-common

%def_without check

Name:    python3-module-%pypi_name
Version: 1.1.28
Release: alt1

Summary: Microsoft Azure Client Library for Python (Common)
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/azure-common/

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-azure-devtools
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc CHANGELOG.md README.md
%python3_sitelibdir/azure/
%python3_sitelibdir/azure_common-%version.dist-info/


%changelog
* Wed Oct 24 2023 Danilkin Danila <danild@altlinux.org> 1.1.28-alt1
- Initial build for Sisyphus
