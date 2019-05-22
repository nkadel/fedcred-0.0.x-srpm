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
%global with_python2 0

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

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
BuildRequires:  python2-beautifulsoup4 >= 4.4.1
BuildRequires:  python2-boto3 >= 1.2.3
BuildRequires:  python2-requests >= 2.8.1
BuildRequires:  python2-requests_ntlm >= 1.0.0
%endif # with_python2
%if 0%{with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-beautifulsoup4 >= 4.4.1
BuildRequires:  python3-boto3 >= 1.2.3
BuildRequires:  python3-requests >= 2.8.1
BuildRequires:  python3-requests_ntlm >= 1.0.0
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
%if 0%{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python2-%{pypi_name}}
%endif # with_python2

%if 0%{with_python3}
%package -n python3-%{pypi_name}
Version:        0.0.2
Release:        0%{?dist}
Url:            https://github.com/broamski/aws-fedcred
Summary:        Get AWS API Credentials When using an Identity Provider/Federation
License:        UNKNOWN (FIXME:No SPDX)
Requires:       python3-beautifulsoup4 >= 4.4.1
Requires:       python3-boto3 >= 1.2.3
Requires:       python3-requests >= 2.8.1
Requires:       python3-requests_ntlm >= 1.0.0
%if 0%{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python3-%{pypi_name}}
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
%description -n python3-%{pypi_name}
fedcred: Obtain AWS API Credentials when using Federation/Identity Providers to authenticate to AWS
===================================================================================================


The following identity providers are currently supported:

* Active Directory Federation Services (ADFS)
* Okta

Installation:
-------------

Option 1
~~~~~~~~
.. code-block:: sh

    $ pip install fedcred

Option 2
~~~~~~~~

.. code-block:: sh

    1. Clone this repo
    2. $ python setup.py install


Config File Setup
----------------------

The configuation file is named ``fedcred.config`` and should exist in the users home directory.

.. code-block:: ini
    
    [fedcred]
    provider = {okta, adfs}
    aws_credential_profile = default
    sslverify = True
    
    [okta]
    organization = <yourorg>.okta.com
    app_url = <okta application url>
    
    [adfs]
    ntlmauth = {True, False}
    url = https://<adfs fqdn>/adfs/ls/idpinitiatedsignon.aspx?loginToRp=urn:amazon:webservices


Usage
-----

.. code-block:: sh

    $ fedcred

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
%{__mv} $RPM_BUILD_ROOT%{_bindir}/${script} $RPM_BUILD_ROOT%{_bindir}/${script}-%{python2_version}
%if ! 0%{with_python3}
%{__ln_s} ${script}-%{python2_version} $RPM_BUILD_ROOT%{_bindir}/${script}
%endif # ! with_python3
%endif # with_python2
%if 0%{with_python3}

%py3_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/${script} $RPM_BUILD_ROOT%{_bindir}/${script}-%{python3_version}
%{__ln_s} ${script}-%{python3_version} $RPM_BUILD_ROOT%{_bindir}/${script}
%endif # with_python3

%clean
rm -rf %{buildroot}

%if 0%{with_python2}
%files -n python2-%{pypi_name}
%defattr(-,root,root,-)
%doc README.rst
%{_bindir}/bin/fedcred-%{python2_version}
%{python2_sitelib}/*
%endif # with_python2

%if 0%{with_python3}
%files -n python3-%{pypi_name}
%defattr(-,root,root,-)
%doc README.rst
%{_bindir}/bin/fedcred-%{python3_version}
%{_bindir}/bin/fedcred
%{python3_sitelib}/*
%endif # with_python3

%changelog
* Wed May 22 2019 Nico Kadel-Garcia <nkadel@gmail.com>
- Store initial setup generated with py2pack
