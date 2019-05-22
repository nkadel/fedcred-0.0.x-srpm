#
# spec file for package python-fedcred
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Single python3 version in Fedora, python3_pkgversion macro for EPEL in older RHEL
%{!?python3_pkgversion:%global python3_pkgversion 3}

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Use python3 only
%global with_python2 0

%global pypi_name fedcred

# Common SRPM package
Name:           python-%{pypi_name}
Version:        0.0.2
Release:        0%{?dist}
Url:            https://github.com/broamski/aws-fedcred
Summary:        Get AWS API Credentials When using an Identity Provider/Federation
License:        UNKNOWN (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/f/fedcred/fedcred-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif # with_python2
%if 0%{with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif # with_python3

%if 0%{with_python2}
%package -n python2-%{pypi_name}
Version:        0.0.2
Release:        0%{?dist}
Url:            https://github.com/broamski/aws-fedcred
Summary:        Get AWS API Credentials When using an Identity Provider/Federation
License:        UNKNOWN (FIXME:No SPDX)
Requires:       python2-beautifulsoup4 >= 4.4.1
Requires:       python2-boto3 >= 1.2.3
Requires:       python2-requests >= 2.8.1
Requires:       python2-requests_ntlm >= 1.0.0
%{?python_provide:%python_provide python2-%{pypi_name}}
%endif # with_python2

%if 0%{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        0.0.2
Release:        0%{?dist}
Url:            https://github.com/broamski/aws-fedcred
Summary:        Get AWS API Credentials When using an Identity Provider/Federation
License:        UNKNOWN (FIXME:No SPDX)
Requires:       python%{python3_pkgversion}-beautifulsoup4 >= 4.4.1
Requires:       python%{python3_pkgversion}-boto3 >= 1.2.3
Requires:       python%{python3_pkgversion}-requests >= 2.8.1
Requires:       python%{python3_pkgversion}-requests_ntlm >= 1.0.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
%endif # with_python3

%description
fedcred: Obtain AWS API Credentials when using Federation/Identity Providers to authenticate to AWS
===================================================================================================


The following identity providers are currently supported:

* Active Directory Federation Services (ADFS)
* Okta

%if 0%{with_python2}
%description -n python2-%{pypi_name}
fedcred: Obtain AWS API Credentials when using Federation/Identity Providers to authenticate to AWS
===================================================================================================


The following identity providers are currently supported:

* Active Directory Federation Services (ADFS)
* Okta

%endif # with_python2

%if 0%{with_python3}
%description -n python%{python3_pkgversion}-%{pypi_name}
fedcred: Obtain AWS API Credentials when using Federation/Identity Providers to authenticate to AWS
===================================================================================================


The following identity providers are currently supported:

* Active Directory Federation Services (ADFS)
* Okta

%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if 0%{with_python2}
%py2_build
%endif # with_python2
%if 0%{with_python3}
%py3_build
%endif # with_python3

%install
%if 0%{with_python2}
%py2_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/fedcred $RPM_BUILD_ROOT%{_bindir}/fedcred-%{python2_version}

%if ! 0%{with_python3}
%
%{__ln_s} fedcred-%{python2_version} $RPM_BUILD_ROOT%{_bindir}/fedcred
%endif # ! with_python3
%endif # with_python2
%if 0%{with_python3}

%py3_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/fedcred $RPM_BUILD_ROOT%{_bindir}/fedcred-%{python3_version}
%{__ln_s} fedcred-%{python3_version} $RPM_BUILD_ROOT%{_bindir}/fedcred
%endif # with_python3

%clean
rm -rf %{buildroot}

%if 0%{with_python2}
%files -n python2-%{pypi_name}
%defattr(-,root,root,-)
%doc README.rst
%{_bindir}/fedcred-%{python2_version}
%{python2_sitelib}/*
%endif # with_python2

%if 0%{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%defattr(-,root,root,-)
%doc README.rst
%{_bindir}/fedcred-%{python3_version}
%{_bindir}/fedcred
%{python3_sitelib}/*
%endif # with_python3

%changelog
* Wec May 22 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 0.0.2-0
- Create initial setup

