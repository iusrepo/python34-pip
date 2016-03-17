%global srcname pip


%global ius_suffix 34u

Name:           python%{ius_suffix}-%{srcname}
Version:        8.1.0
Release:        1.ius%{?dist}
Summary:        A tool for installing and managing Python packages
Group:          Development/Libraries
License:        MIT
URL:            https://pip.pypa.io
Source0:        https://pypi.python.org/packages/source/p/pip/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python%{ius_suffix}-devel
BuildRequires:  python%{ius_suffix}-setuptools
Requires:       python%{ius_suffix}-setuptools


%description
Pip is a replacement for `easy_install
<http://peak.telecommunity.com/DevCenter/EasyInstall>`_.  It uses mostly the
same techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.


%prep
%setup -q -n %{srcname}-%{version}
find %{srcname} -type f -name \*.py -print0 | xargs -0 sed -i -e '1 {/^#!\//d}'


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install \
    --root %{buildroot} \
    --optimize 1 \
    --skip-build

# delete pip and pip3
%{__rm} -f %{buildroot}%{_bindir}/pip
%{__rm} -f %{buildroot}%{_bindir}/pip3
# symlink pip3 to pip3.4
ln -sf %{_bindir}/%{srcname}%{python3_version} %{buildroot}%{_bindir}/%{srcname}3


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc README.rst docs
%{_bindir}/pip3
%{_bindir}/pip%{python3_version}
%{python3_sitelib}/pip*


%changelog
* Thu Mar 17 2016 Carl George <carl.george@rackspace.com> - 8.1.0-1.ius
- Latest upstream
- Remove build_wheel
- Strip shebangs
- Use %%license when possible
- Macro clean up

* Fri Jan 22 2016 Ben Harper <ben.harper@rackspace.com> - 8.0.2-1.ius
- Latest upstream

* Fri Jan 22 2016 Ben Harper <ben.harper@rackspace.com> - 8.0.1-2.ius
- correct patch0

* Thu Jan 21 2016 Ben Harper <ben.harper@rackspace.com> - 8.0.1-1.ius
- Latest upstream
- Refresh patch0

* Mon Aug 24 2015 Ben Harper <ben.harper@rackspace.com> - 7.1.2-1.ius
- Latest upstream

* Fri Aug 21 2015 Ben Harper <ben.harper@rackspace.com> - 7.1.1-1.ius
- Latest upstream

* Thu Jul 02 2015 Ben Harper <ben.harper@rackspace.com> - 7.1.0-1.ius
- Latest upstream

* Mon Jun 08 2015 Carl George <carl.george@rackspace.com> - 7.0.3-1.ius
- Latest upstream

* Fri May 22 2015 Carl George <carl.george@rackspace.com> - 7.0.0-1.ius
- Latest upstream
- Refresh patch0

* Tue Apr 07 2015 Carl George <carl.george@rackspace.com> - 6.1.1-1.ius
- Latest upstream
- Refresh patch0

* Thu Feb 05 2015 Ben Harper <ben.harper@rackspace.com> - 6.0.8-1.ius
- Latest sources from upstream

* Thu Jan 29 2015 Carl George <carl.george@rackspace.com> - 6.0.7-1.ius
- Latest upstream

* Mon Jan 05 2015 Carl George <carl.george@rackspace.com> - 6.0.6-1.ius
- Latest upstream

* Fri Dec 26 2014 Carl George <carl.george@rackspace.com> - 6.0.3-1.ius
- Latest upstream
- Refresh patch0

* Wed Aug 13 2014 Carl George <carl.george@rackspace.com> - 1.5.6-3.ius
- Make pip3 a symlink to pip3.4
- Enable wheel

* Tue Aug 12 2014 Carl George <carl.george@rackspace.com> - 1.5.6-2.ius
- Port from Fedora to IUS
- Update Patch0 for latest source

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.6-1
- Update to 1.5.6

* Fri Apr 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-4
- Rebuild as wheel for Python 3.4

* Thu Apr 24 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-3
- Disable build_wheel

* Thu Apr 24 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-2
- Rebuild as wheel for Python 3.4

* Mon Apr 07 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-1
- Updated to 1.5.4

* Mon Oct 14 2013 Tim Flink <tflink@fedoraproject.org> - 1.4.1-1
- Removed patch for CVE 2013-2099 as it has been included in the upstream 1.4.1 release
- Updated version to 1.4.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-4
- Fix for CVE 2013-2099

* Thu May 23 2013 Tim Flink <tflink@fedoraproject.org> - 1.3.1-3
- undo python2 executable rename to python-pip. fixes #958377
- fix summary to match upstream

* Mon May 06 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.3.1-2
- Fix main package Summary, it's for Python 2, not 3 (#877401)

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.1-1
- Update to 1.3.1, fix for CVE-2013-1888.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-2
- Fixing files for python3-pip

* Thu Oct 04 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-1
- Update to upstream 1.2.1
- Change binary from pip-python to python-pip (RHBZ#855495)
- Add alias from python-pip to pip-python, to be removed at a later date

* Tue May 15 2012 Tim Flink <tflink@fedoraproject.org> - 1.1.0-1
- Update to upstream 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- update to 1.0.2 and added python3 subpackage

* Wed Jun 22 2011 Tim Flink <tflink@fedoraproject.org> - 0.8.3-1
- update to 0.8.3 and project home page

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Luke Macken <lmacken@redhat.com> - 0.8.2-1
- update to 0.8.2 of pip
* Mon Aug 30 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.8-1
- update to 0.8 of pip
* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 7 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.2-1
- update to 0.7.2 of pip
* Sun May 23 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.1-1
- update to 0.7.1 of pip
* Fri Jan 1 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1.4
- fix dependency issue
* Fri Dec 18 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-2
- fix spec file 
* Thu Dec 17 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-1
- upgrade to 0.6.1 of pip
* Mon Aug 31 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.4-1
- Initial package

